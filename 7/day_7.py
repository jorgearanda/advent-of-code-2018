def load():
    split_reqs = [req.strip().split() for req in open('input.txt', 'r')]

    reqs = {}
    for req in split_reqs:
        dep = req[1]
        target = req[7]
        if dep not in reqs:
            reqs[dep] = set()
        if target not in reqs:
            reqs[target] = set()
        reqs[target].add(dep)

    return reqs


def duration(task):
    return ord(task) - 4  # ord('A') is 65, and 'A' should return 61


def part_1():
    reqs = load()
    steps = sorted(reqs)

    progression = ''
    while len(steps) > 0:
        clear = [step for step in steps if len(reqs[step]) == 0]
        next = clear[0]
        progression += next
        reqs.pop(next)
        steps.remove(next)
        for req in reqs:
            if next in reqs[req]:
                reqs[req].remove(next)

    print('Part 1:', progression)


class Worker():
    def __init__(self):
        self.task = None
        self.seconds_to_idle = 0

    def tick(self):
        if self.seconds_to_idle > 1:
            self.seconds_to_idle -= 1
            return None
        elif self.seconds_to_idle == 1:
            self.seconds_to_idle = 0
            completed = self.task
            self.task = None
            return completed
        else:
            pass

    def is_idle(self):
        return self.task is None

    def assign_task(self, task):
        self.task = task
        self.seconds_to_idle = duration(task)


def find_idle(workers):
    for worker in workers:
        if worker.is_idle():
            return worker
    return None


def find_working(workers):
    for worker in workers:
        if not worker.is_idle():
            return worker
    return None


def part_2():
    reqs = load()
    steps = sorted(reqs)

    seconds = 0
    progression = ''
    workers = [Worker() for _ in range(5)]

    while len(reqs) > 0:
        clear = [step for step in steps if len(reqs[step]) == 0]
        while len(clear) > 0 and find_idle(workers) is not None:
            next = clear.pop(0)
            steps.remove(next)
            idle_worker = find_idle(workers)
            idle_worker.assign_task(next)

        seconds += 1
        for worker in workers:
            completed = worker.tick()
            if completed:
                progression += completed
                reqs.pop(completed)
                for req in reqs:
                    if completed in reqs[req]:
                        reqs[req].remove(completed)

    print('Part 2:', seconds)


part_1()
part_2()
