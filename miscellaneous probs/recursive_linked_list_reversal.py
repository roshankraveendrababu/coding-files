class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    if head is None or head.next is None:
        return head

    p = reverseList(head.next)
    head.next.next = head
    head.next = None

    return p

# Helper functions to create and print linked lists
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_linked_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(" -> ".join(map(str, values)) + " -> None")

# Main function
def main():
    # Test case with 7 elements
    values = [10, 20, 30, 40, 50, 60, 70]
    print("Original List:")
    head = create_linked_list(values)
    print_linked_list(head)

    # Reverse the list using recursive function
    reversed_head = reverseList(head)
    print("Reversed List:")
    print_linked_list(reversed_head)

if __name__ == "__main__":
    main()
