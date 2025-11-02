

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next

        current.next = new_node


    def get_at_position(self, position):
        if position < 1:
            return None
        
        current = self.head
        index = 1

        while current:
            if index == position:
                return current.value
            current = current.next
            index += 1
        return None


    def delete_at_position(self, position):
        if position < 1 or self.head is None:
            raise IndexError("Invalid position")
        
        if position == 1:
            self.head = self.head.next
            return
        
        prev = self.head
        index = 1
        while prev and index < position - 1:
            prev = prev.next
            index += 1

        if prev is None or prev.next is None:
            raise IndexError("Invalid position")
        
        prev.next = prev.next.next


    def size(self):
        count, cur = 0, self.head
        while cur:
            count += 1
            cur = cur.next
        return count



class Task:
    def __init__(self, name):
        self.name = name
        self.complete = False

    def __str__(self):
        box = "✅" if self.complete else "🟧"
        status = "complete" if self.complete else "incomplete"
        return f"{box} {self.name} - {self.complete}"
    

class ToDoList:
    def __init__(self, list_name="My Tasks"):
        self.list_name = list_name
        self.tasks = LinkedList()

    def add_task(self, task_name):
        new_task = Task(task_name)
        self.tasks.append(new_task)
        print(f"Added: '{task_name}'")

    def complete_task(self, position):
        task = self.tasks.get_at_position(position)
        if task is None:
            return False
        
        task.complete = True
        return True
    
    def remove_task(self, position):
        try:
            self.tasks.delete_at_position(position)
            return True
        
        except Exception:
            return False
        
    def view_all_tasks(self):
        print(self.list_name)
        print("=" * len(self.list_name))

        total = self.tasks.size()
        if total == 0:
            print("No tasks yet")
            return
        
        for i in range(1, total + 1):
            task = self.tasks.get_at_position(i)
            print(f"{i}. {task}")

    def view_incomplete_tasks(self):
        title = f"{self.list_name} Incomplete"
        print(title)
        print("=" * len(title))

        t_left = 0
        idx = 1
        while True:
            task = self.tasks.get_at_position(idx)
            if task is None:
                break

            if not task.complete:
                t_left += 1
                print(f"{t_left}. {task}")
            idx += 1

        if t_left == 0:
            print("All tasks complete!")


    def get_task_count(self):
        return self.tasks.size()
    
    def get_completion_stats(self):
        complete = 0
        incomplete = 0
        idx = 1
        while True:
            task = self.taks.get_at_position(idx)
            if task is None:
                break

            if task.complete:
                complete += 1

            else:
                incomplete += 1

            idx += 1
        total = complete + incomplete
        percent = (complete / total * 100) if total else 0.0
        return complete, incomplete, round(percent, 1)
    

def test_todo_list():
    """Test function to verify ToDoList functionality"""
    print("=== Testing To-Do List Implementation ===\n")
    
    # Create a new to-do list
    todo = ToDoList("School Tasks")
    
    # Test adding tasks
    print("1. Adding tasks...")
    todo.add_task("Study for math exam")
    todo.add_task("Write history essay")
    todo.add_task("Submit science project")
    todo.add_task("Read chapter 5")
    
    # Test viewing all tasks
    print("\n2. Viewing all tasks:")
    todo.view_all_tasks()
    
    # Test completing tasks
    print("\n3. Completing some tasks...")
    todo.complete_task(2)  # Complete second task
    todo.complete_task(4)  # Complete fourth task
    
    # Test viewing after completion
    print("\n4. Viewing tasks after completion:")
    todo.view_all_tasks()
    
    
    # Test removing tasks
    print("\n5. Removing a task...")
    todo.remove_task(3)  # Remove third task
    todo.view_all_tasks()
    
    # Test edge cases
    print("\n6. Testing edge cases...")
    print("Trying to complete task at invalid position:")
    result = todo.complete_task(10)  # Position that doesn't exist
    print(f"Result: {result}")
    
    print("Trying to remove task at invalid position:")
    result = todo.remove_task(0)  # Invalid position (should be 1-indexed)
    print(f"Result: {result}")
    
    print("\n=== Test completed! ===")


test_todo_list()