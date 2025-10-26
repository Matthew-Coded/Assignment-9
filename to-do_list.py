

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


def test_todo_list():
    print("=== Testing To-Do List ===\n")

    todo = ToDoList("School Tasks")

    print("1. Adding Tasks...")
    todo.add_task("Study for math exam")
    todo.add_task("Write history essay")
    todo.add_task("Turn in science project")
    todo.add_task("Read chapter 5")

    print("\n2. Viewing all tasks:")
    todo.view_all_tasks()

    print("\n3. Completing some tasks")
    print("Complete #2:", todo.complete_task(2))
    print("Complete #4:", todo.complete_task(4))

    print("\n4. View tasks after completing")
    todo.view_all_tasks()

    print("\n 5. Removing a task")
    print("Remove #3:", todo.remove_task(3))
    todo.view_all_tasks()

    print("\n6. Testing invalid tasks")
    print("Complete invalid #10:", todo.complete_task(10))
    print("Remove invalid #0:", todo.remove_task(0))

    print("\n=== Testing Complete ===")

if __name__ == "__main__":
    test_todo_list()