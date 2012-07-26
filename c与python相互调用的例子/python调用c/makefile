CC=g++
CFLAG= -shared -fpic
LIBS=

TARGET=MyCppModule.so

$(TARGET):test.cpp
	$(CC) $(CFLAG) $(LIBS) $< -o $@

clean:
	@rm -f $(TARGET)
