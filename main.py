import json
import logging
from pprint import pformat
import os
from collections import defaultdict
import quixstreams
import requests_sse


logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s (%(filename)s:%(lineno)d)")

"""Types of events:
CreateEvent
DeleteEvent
ForkEvent
GollumEvent
IssueCommentEvent
IssuesEvent
MemberEvent
PullRequestEvent
PullRequestReviewEvent
PushEvent
ReleaseEvent
WatchEvent
"""

def handle_stats(stats_msg: str) -> None:
    stats = json.loads(stats_msg)
    logging.info("STATS: %s", pformat(stats))

def main():
    logging.info("Initializing Github Firehose Quixio project")

    app = quixstreams.Application(
        broker_address="localhost:19092",
        loglevel="DEBUG",
        producer_extra_config={
            "statistics.interval.ms": 3 * 1000,
            "stats_cb": handle_stats,
        #     "debug": "msg",
        #     "linger.ms": 200,
        #     "compression.type": "gzip",
        },
    )

    events = defaultdict(int)
    with (
        app.get_producer() as producer,
        requests_sse.EventSource(
            "http://github-firehose.libraries.io/events",
            timeout=30,
        ) as event_source,
    ):
        for event in event_source:
            logging.debug(f"Received event: {pformat(event)}")
            data = json.loads(event.data)
            logging.debug(f"Received data: {pformat(data)}")
            event_type = data.get("type",None)
            events[event_type] += 1
            event_actor = data.get("actor",None)
            event_repo = data.get("repo",None)
            key = data["id"]
            logging.debug("Got: %s", pformat(data))

            producer.produce(
                topic="github_events",
                key=key,
                value=json.dumps(data),
            )

if __name__ == "__main__":
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    try:
        main()
    except KeyboardInterrupt:
        pass