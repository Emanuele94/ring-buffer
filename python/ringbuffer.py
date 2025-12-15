# class RingBuffer:
#     def __init__(self, capacity):
#         """
#         Inizializza il buffer.
#         :param capacity: La dimensione massima del buffer.
#         """
#         self.capacity = capacity
#         self.buffer = [None] * capacity  # Creiamo la lista vuota di dimensione fissa
#         self.head = 0  # Indice di scrittura
#         self.tail = 0  # Indice di lettura
#         self.size = 0  # Quanti elementi ci sono attualmente

#     def is_empty(self):
#         return self.size == 0

#     def is_full(self):
#         return self.size == self.capacity

#     def enqueue(self, item):
#         """Aggiunge un elemento (Scrittura)"""
#         if self.is_full():
#             # Qui c'è una scelta di design:
#             # 1. Lanciamo un errore?
#             # 2. Sovrascriviamo il vecchio (comportamento tipico del Ring Buffer)?
#             # Scegliamo l'opzione 2: Sovrascrivere!
            
#             print(f"Overwriting old data: {self.buffer[self.tail]}")
#             # Se sovrascriviamo, la coda deve avanzare perché il vecchio dato è perso!
#             self.tail = (self.tail + 1) % self.capacity
#             self.size -= 1 # Tecnicamente rimuoviamo uno per aggiungerne uno
        
#         self.buffer[self.head] = item
        
#         # IL TRUCCO MAGICO: L'operatore Modulo (%)
#         # Se capacity è 5 e head è 4, (4+1) % 5 diventa 0!
#         self.head = (self.head + 1) % self.capacity
#         self.size += 1
#         print(f"Enqueued: {item}")

#     def dequeue(self):
#         """Rimuove e restituisce l'elemento più vecchio (Lettura)"""
#         if self.is_empty():
#             print("Buffer is empty! Cannot dequeue.")
#             return None
        
#         item = self.buffer[self.tail]
#         self.buffer[self.tail] = None # Opzionale: pulizia visiva
        
#         # Avanziamo la coda circolarmente
#         self.tail = (self.tail + 1) % self.capacity
#         self.size -= 1
#         return item

#     def __str__(self):
#         """Per stampare lo stato del buffer in modo carino"""
#         return f"Buffer: {self.buffer} | Head: {self.head} | Tail: {self.tail} | Size: {self.size}"

# # --- TEST DRIVE ---
# if __name__ == "__main__":
#     # Creiamo un buffer piccolo per vedere cosa succede
#     rb = RingBuffer(5)
    
#     print("--- Filling the buffer ---")
#     rb.enqueue("A")
#     rb.enqueue("B")
#     rb.enqueue("C")
#     rb.enqueue("D")
#     rb.enqueue("E")
#     print(rb)
    
#     print("\n--- Overwriting (The Magic Moment) ---")
#     # Il buffer è pieno. Aggiungendo "F", dovremmo perdere "A"
#     rb.enqueue("F") 
#     print(rb) # Notate che "A" è sparito e "F" è al suo posto (indice 0)
    
#     print("\n--- Reading ---")
#     print(f"Read: {rb.dequeue()}") # Dovrebbe leggere "B", perché "A" è stato sovrascritto
#     print(rb)


from collections import deque

class RingBuffer:
    def __init__(self, capacity):
        self.buffer = deque(maxlen=capacity)

    def enqueue(self, item):
        if len(self.buffer) == self.buffer.maxlen:
            print(f"Overwriting old data: {self.buffer[0]}")
        self.buffer.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if not self.buffer:
            print("Buffer is empty! Cannot dequeue.")
            return None
        return self.buffer.popleft()

    def __str__(self):
        return f"Buffer: {list(self.buffer)} | Size: {len(self.buffer)}"