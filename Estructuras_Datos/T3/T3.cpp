#include <iostream>

using namespace std;

class ColaLineal
{
private:
    int arr[5];
    int front, rear = -1;

public:
    void enqueue(int x)
    {
        if (rear == 4)
        {
            cout << "Cola llena" << endl;
        }
        else
        {
            rear++;
            arr[rear] = x;
        }
    }
    void dequeue()
    {
        if (front > rear)
        {
            cout << "Cola vacia" << endl;
        }
        else
        {
            front++;
        }
    }
};

class ColaCircular
{
    private:
    int arr[5];
    int front, rear = -1;
    public:
    void enqueue(int x)
    {
        int next = (rear + 1) % 5;
        if (next == front) {
            cout << "Cola llena" << endl;
            return;
        }

        if (front == -1) {
            front, rear = 0;
        }

        arr[rear] = x;
        cout << "Insertado: " << x << endl;
    }
};
int main()
{
    ColaLineal cola;
    cola.enqueue(10);
    cola.enqueue(20);
    cola.enqueue(20);
    cola.enqueue(20);
    cola.enqueue(20);
    cola.dequeue();
    cola.dequeue();
    cola.enqueue(30);
    return 0;
}