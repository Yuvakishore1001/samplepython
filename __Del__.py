class mydel():
    def __del__(self):
        print("destroyed")

c1=mydel()
c2=mydel()

# c1=print(mydel())
# c2=print(mydel())