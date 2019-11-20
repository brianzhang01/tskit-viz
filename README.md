# tskit-viz

Trying out a visualization idea for `tskit.TreeSequence`

![Demo video](static/tskit-viz-demo.mp4)

## Earlier proposal

Given N samples, there are N! ways to order them. Given a local tree for these samples, there are 2^(N-1) ways to order the samples left-to-right such that the resulting tree can be drawn in the canonical way without intersections.

Side note: does this mean there are N! / 2^(N-1) possible rooted trees?
- N = 1: (1)
- N = 2: (1 2)
- N = 3: (1 (2 3)), (2 (1 3)), (3 (1 2))

Answer: no, because given a sample order, there are multiple resulting local trees.

Out of these 2^(N-1) sample orderings, let us use a convention where we always choose the one with lowest lexicographic sort order. When we slide along the genome and a recombination event occurs, this corresponds to a SPR (subtree pruning and regrafting). Because of the lexicographic sort order, the change from the SPR can be illustrated by taking two neighboring list of samples and rearranging them, while keeping the individual lists in the same order:
```
a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9
    |              |         |
                  <->
    |         |              |
a_1, a_5, a_6, a_2, a_3, a_4, a_7, a_8, a_9
```

We propose to show this as either an animation or an interactive PyGame applet that moves between neighboring trees, illustrating the effects of the SPR. In the case of the PyGame applet, we can use the up-down arrows to move forward and backward along the genomes.
