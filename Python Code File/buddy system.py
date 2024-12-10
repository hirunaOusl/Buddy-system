class BuddySystem:
    def __init__(self, total_memory):
        self.total_memory = total_memory
        self.free_blocks = {total_memory: [0]}  
        self.allocated_blocks = {}  
        
    def allocate(self, size):
        block_size = 1
        while block_size < size:
            block_size *= 2

        # Find the smallest suitable block
        for size_key in sorted(self.free_blocks.keys()):
            if size_key >= block_size and self.free_blocks[size_key]:
                address = self.free_blocks[size_key].pop(0)
                print(f"Allocated {block_size} KB at address {address}")

                # Split larger blocks into smaller blocks if necessary
                while size_key > block_size:
                    size_key //= 2
                    buddy_address = address + size_key
                    if size_key not in self.free_blocks:
                        self.free_blocks[size_key] = []
                    self.free_blocks[size_key].append(buddy_address)

                # Track the allocated block
                self.allocated_blocks[address] = block_size
                return address

        print("Memory allocation failed: Not enough memory!")
        return None

    def show_blocks(self):
        # Display allocated and free blocks
        print("\nAllocated Blocks:")
        for address, size in sorted(self.allocated_blocks.items()):
            print(f"{size} KB (allocated) at address {address}")

        print("\nFree Blocks:")
        for size, addresses in sorted(self.free_blocks.items()):
            for address in addresses:
                print(f"{size} KB (free) at address {address}")

if __name__ == "__main__":
    total_memory = 1024  # memory size (in KB)
    buddy = BuddySystem(total_memory)

    while True:
        print("\nOptions:")
        print("1. Allocate Memory")
        print("2. Show Free Blocks")
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            size = int(input("Enter memory size to allocate: "))
            buddy.allocate(size)
        elif choice == "2":
            buddy.show_blocks()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please try again.")
