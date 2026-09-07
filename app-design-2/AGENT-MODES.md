# Agent modes — App Design 2

Five words. Type one at the start of a message and the agent behaves that way for the reply.
They exist so you can choose how much help you are getting, on purpose, instead of drifting
into letting it write everything.

| Word | What the agent does | When it is the right call |
|---|---|---|
| `EXPLAIN` | Explains your own code back to you, then asks you questions about it. Writes no new code. | You got it working and you are not sure why. |
| `REVIEW` | Reads what you already wrote and names things it would change, with reasons. Does not rewrite. | You are done and want it to be better. |
| `DEBUG` | Helps you *find* the bug. Narrows it down, asks what you have tried, points at the region. **Does not fix it.** | Something is broken and you want to stay the one who fixes it. |
| `PAIR` | Builds with you in small steps you approve one at a time. | New territory, and you want to move. |
| `SPEC` | You write the specification, it builds exactly that and reports where your spec was vague. | You want to find out whether you can describe a thing precisely. |

## Why the words exist

Left alone, an agent will write the whole thing, and you will ship something you could not have
written and cannot debug. Naming the mode is you deciding, before you ask, how much of the
thinking you are keeping.

`DEBUG` is the one to reach for most. Finding a bug is the actual skill; typing the fix is not.

## Say what the agent did

Every commit carries one line at the end saying which mode you used:

    Agent: none        you wrote it
    Agent: explain     it explained, you wrote
    Agent: review      you wrote, it reviewed
    Agent: debug       it helped you find, you fixed
    Agent: pair        you built it together
    Agent: spec        you specified, it built

This is not a gotcha. It is the record of how you worked, it is readable from the repo without
anyone being asked, and at the end of the year it is the most interesting thing in your history —
you will be able to see the point where you stopped needing `PAIR`.
