CC = /usr/bin/gcc
CFLAGS = -Wall -g --std=c99
LDFLAGS =

BUILDDIR = build

all: clean dummy_gps

clean:
	rm -rf $(BUILDDIR)/*

dummy_gps: $(BUILDDIR)/dummy_gps_generator.o
	$(CC) $(CFLAGS) -o $(BUILDDIR)/dummy_gps_generator $< $(LDFLAGS)

$(BUILDDIR)/%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@