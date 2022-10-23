struct ListNode
{
    int val;
    ListNode *next;
};

class MyLinkedList
{
private:
    int size = 0;
    ListNode *next = nullptr;

public:
    MyLinkedList()
    {
    }

    int get(int index)
    {
        if (index < 0 || index >= this->size)
            return -1;
        ListNode *node = this->next;
        for (int i = 0; i < index; i++)
            node = node->next;
        return node->val;
    }

    void addAtHead(int val)
    {
        ListNode *pre;
        ListNode *node;
        node->val = val;
        node->next =
    }

    void addAtTail(int val)
    {
    }

    void addAtIndex(int index, int val)
    {
    }

    void deleteAtIndex(int index)
    {
    }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */