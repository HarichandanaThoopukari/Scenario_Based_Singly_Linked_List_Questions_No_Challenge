class Node:
    def __init__(self,song):
        self.song=song
        self.next=None
class singlylinkedlist:
    def __init__(self):
        self.head=None
    def insert_at_begin(self,song):
        newnode=Node(song)
        if self.head is None:
            self.head=newnode
            return
        newnode.next=self.head
        self.head=newnode
    def insert_at_end(self,song):
        newnode=Node(song)
        if self.head is None:
            self.head=newnode
            return
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=newnode
    def insert_at_any_pos(self,song,pos):
        if pos<=0:
            print("Invalid position")
            return
        if pos==1:
            self.insert_at_begin(song)
            return
   
        temp=self.head
        i=1
        while i<pos-1 and temp is not None:
            temp=temp.next
            i+=1
        if temp is None:
            print("Insufficient Songs")
            return
        newnode=Node(song)
        newnode.next=temp.next
        temp.next=newnode
    def count(self):
        ct=0
        temp=self.head
        while temp is not None:
            ct+=1
            temp=temp.next
        return ct
    def insert_at_mid(self,song):
        n=self.count()
        mid=n//2+1
        self.insert_at_any_pos(song,mid)
        return
    def delete_at_begin(self):
        if self.head is None:
            print("Playlist is Empty")
            return
        self.head=self.head.next
    def delete_at_End(self):
        if self.head is None:
            print("playlist is Empty")
            return
        
        temp=self.head
        prev=None
        while temp.next is not None:
            prev=temp
            temp=temp.next
        prev.next=None
    def delete_at_any_position(self,pos):
        if pos<=0:
            print("invalid position")
            return
        if pos==1:
            self.delete_at_begin()
            return
        i=1
        temp=self.head
        prev=None
        while i<pos and temp is not None:
            prev=temp
            temp=temp.next
            
            i+=1
        if temp is None:
            print("Insufficient Song")
            return
        prev.next=temp.next
    def delete_at_mid(self):
        n=self.count()
        mid=n//2+1
        self.delete_at_any_position(mid)
    def search(self,target_song):
        
        temp=self.head
        pos=1
        while temp is not None:
           
            if temp.song==target_song:
                print("Song is Found at",pos)
                return
            temp=temp.next
            pos+=1
        return -1
    def display(self):
        if self.head is None:
            print("Playlist is Empty")
            return
        temp=self.head
        while temp is not None:
            if temp.next:
                print(temp.song,end=" -> ")
            else:
                print(temp.song,end="")
            temp=temp.next
    def reverse(self):
        prev=None
        temp=self.head
        while temp is not None:
            nextnode=temp.next
            temp.next=prev
            prev=temp
            temp=nextnode
        self.head=prev
ll=singlylinkedlist()
while True:
    print("\n1. Add a song to the beginning of the playlist")
    print("2. Add a song to the end of the playlist")
    print("3. Insert a song at a specified position")
    print("4. Remove the first song from the playlist")
    print("5. Remove the last song from the playlist")
    print("6. Remove the song at a specified position")
    print("7. Search for a song and display its position")
    print("8. Display the total number of songs")
    print("9. Display the complete playlist")
    print("10. Reverse the playlist order")
    print("11. Exit")
    choice = int(input("Enter choice:"))
    match choice:
        case 1:
            song=input("Enter song:")
            ll.insert_at_begin(song)
        case 2:
            song=input("Enter song")
            ll.insert_at_end(song)
        case 3:
            song=input("Enter song")
            pos=int(input("Enter position:"))
            ll.insert_at_any_pos(song,pos)
        case 4:
            ll.delete_at_begin()
        case 5:
            ll.delete_at_End()
        case 6:
            pos=int(input("Enter position:"))
            ll.delete_at_any_position(pos)
        case 7:
            target_song=input("Enter Song:")
            ll.search(target_song)
        case 8:
            print("Number of Songs in the Playlist",ll.count())
        case 9:
            ll.display()
        case 10:
            ll.reverse()
            print("playlist is reversed")
            ll.display()
        case 11:
            print("program terminated")
            break
        case _ :
            print("Invalid Choice")
        
            
            
    
            
            
                
                
        
        
        
        
            
        
            
        
            
        
        
        
    
    
        
        
            
        
            
        
        