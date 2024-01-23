#pragma once
#include <iostream>
#include <stdexcept>

template <typename T>
class ListNode {
public:
    T data;
    ListNode* prev;
    ListNode* next;

    ListNode(const T& value) : data(value), prev(nullptr), next(nullptr) {}
};

template <typename T>
class List {
private:
    ListNode<T>* head;
    ListNode<T>* tail;

public:
    List() : head(nullptr), tail(nullptr) {}

    void pushBack(const T& value) {
        ListNode<T>* newNode = new ListNode<T>(value);
        if (!head) {
            head = tail = newNode;
        }
        else {
            newNode->prev = tail;
            tail->next = newNode;
            tail = newNode;
        }
    }

    std::size_t size() const {
        std::size_t count = 0;
        ListNode<T>* current = head;
        while (current) {
            ++count;
            current = current->next;
        }
        return count;
    }

    void removeLast() {
        if (tail) {
            ListNode<T>* lastNode = tail;
            tail = lastNode->prev;
            if (tail) {
                tail->next = nullptr;
            }
            else {
                head = nullptr;
            }
            delete lastNode;
        }
    }

    ListNode<T>* getTail() const {
        return tail;
    }

    ~List() {
        ListNode<T>* current = head;
        while (current) {
            ListNode<T>* next = current->next;
            delete current;
            current = next;
        }
    }
};

template <typename T>
class Stack {
private:
    List<T> list;

public:
    Stack() {}

    ~Stack() {}

    void push(const T& value) {
        list.pushBack(value);
    }

    void pop() {
        if (list.size() > 0) {
            list.removeLast();
        }
        else {
            throw std::out_of_range("Stack is empty");
        }
    }


    T getTop() const {
        if (list.size() > 0) {
            return list.getTail()->data;
        }
        else {
            throw std::out_of_range("Stack is empty");
        }
    }
};
