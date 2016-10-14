C = gcc
FLAGS = -Wall -O2 -g
LFLAGS = -g
PROG = t1.out

OBJECTS = $(OBJECT_MAIN)

OBJECT_MAIN = problem1.o

FILE_MAIN = problem1.c

$(PROG): $(OBJECTS)
	$(C) -o $(PROG) $(OBJECTS) $(LFLAGS)

$(OBJECT_MAIN): $(FILE_MAIN)
	$(C) -o $(OBJECT_MAIN) -c $(FILE_MAIN) $(FLAGS)

run: $(PROG)
	./$(PROG)
clean:
	rm $(OBJECTS)