- install fio
- run script.sh in a directory containing a largefile named 'testfile'

Hint to create a largefile:
Create a file named 'testfile' with some contents. Then run
	for i in {1..25}; do cat testfile testfile > file2 && mv file2 testfile; done
You can tune the loop counter to control the size of the file


- after running script.sh, 4 files (randread 4K, randread 8K, randwrite 4K, randwrite 8K) will be generated : out_r4.txt, out_r8.txt, out_w4.txt, out_w8.txt

- Use the parser to clean it. Change filenames in line 22, 23 of parser.cc and make it. Run ./parser and view the cleaned output.
