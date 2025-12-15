from ringbuffer import RingBuffer 

# --- TEST DRIVE ---
if __name__ == "__main__":
    rb = RingBuffer(5)
    
    print("--- Filling the buffer ---")
    rb.enqueue("A")
    rb.enqueue("B")
    rb.enqueue("C")
    rb.enqueue("D")
    rb.enqueue("E")
    print(rb)
    
    print("\n--- Overwriting (The Magic Moment) ---")
    rb.enqueue("F") 
    print(rb)
    
    print("\n--- Reading ---")
    print(f"Read: {rb.dequeue()}") 
    print(rb)