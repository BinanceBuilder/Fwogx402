"""Fwogx402 两栖核心循环占位实现"""
import time
import argparse

class AmphibiousCore:
    def __init__(self, mode: str = "observe") -> None:
        self.mode = mode

    def stream(self):
        while True:
            frame = {"height": 0, "dummy": True}
            yield frame
            time.sleep(3)

    def propose(self, frame):
        return {"state": frame, "budget": {"max_notional": 0}, "tags": ["placeholder"], "constraints": ["read_only"]}

    def report(self, intent):
        print("[Fwogx402] intent", intent)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", default="observe")
    args = parser.parse_args()
    core = AmphibiousCore(mode=args.mode)
    for frame in core.stream():
        intent = core.propose(frame)
        core.report(intent)

if __name__ == "__main__":
    main()
