# mmt
A test tool for kernel mm test benchmark.

# idea
I have took a long time to search a tool to measure the performance of
MM in kernel. And there is already one which is gorman's mmtests.

But the framework is not suitable in android.

So I decide to write one.
# Struct
- bin  
The binary for test.

- config  
The config data for draw and test.

- draw  
Use python matplotlib to do some graph.

- driver  
The code add need added in kernel.

- file  
The input data and file operate ops.
