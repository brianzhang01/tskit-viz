# THIS REPOSITORY IS DEPRECATED

Files have been moved to be part of the https://github.com/tskit-dev/tsviz/ project instead. Please do not develop here.

## tskit-viz

Trying out a visualization idea for `tskit.TreeSequence`

![Demo video](static/tskit-viz-demo.gif)

## Earlier proposal

Given N samples, there are N! ways to order them. Given a local tree for these samples, there are 2^(N-1) ways to order the samples left-to-right such that the resulting tree can be drawn in the canonical way without intersections.

Out of these 2^(N-1) sample orderings, let us use a convention where we always choose the one with lowest lexicographic sort order. When we slide along the genome and a recombination event occurs, this corresponds to a SPR (subtree pruning and regrafting). Because of the lexicographic sort order, the change from the SPR can be illustrated by taking two neighboring list of samples and rearranging them. Usually, this operation will keep the individual lists in roughly the same order:
```
a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9
    |              |         |
                  <->
    |         |              |
a_1, a_5, a_6, a_2, a_3, a_4, a_7, a_8, a_9
```

(For an example where the simple slide operation fails, run `python make_example.py` followed by `python viz.py --file example.trees --sort 1`. By comparing with `python viz.py --file example.trees --sort 0`, we see that sometimes our sorting makes things worse.)

We propose to show this as either an animation or an interactive PyGame applet that moves between neighboring trees, illustrating the effects of the SPR. In the case of the PyGame applet, we can use the left-right arrows to move forward and backward along the genomes.
