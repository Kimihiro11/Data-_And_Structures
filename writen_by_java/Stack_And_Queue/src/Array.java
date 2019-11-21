public class Array<E> {
    private int size;
    private E[] data;

    // 构造函数
    public Array(int capacity) {
        data = (E[]) new Object[capacity];
        size = 0;
    }

    //无参构造函数
    public Array() {
        this(10);
    }

    //获取数组容量
    public int getCapacity() {
        return data.length;
    }

    // 获取数组中元素个数
    public int getSize() {
        return size;
    }

    // 数组判空
    public boolean isEmpty() {
        return size == 0;
    }

    //  在index 索引处 插入元素 e
    public void add(int index, E e) {
        judgeIndex(index);
        if (size == data.length)
            reSize(2 * data.length);
        for (int i = size - 1; i >= index; i--)
            data[i + 1] = data[i];
        data[index] = e;
        size++;
    }

    //数组尾部添加元素
    public void addLast(E e) {
        add(size, e);
    }

    //数组头部添加元素
    public void addFirst(E e) {
        add(0, e);
    }

    // 获取index索引处元素
    public E get(int index) {
        judgeIndex(index);
        return data[index];
    }

    public E getLast() {
        return get(size - 1);
    }

    public E getFirst() {
        return get(0);
    }

    // 修改 索引index 处元素为e
    public void set(int index, E e) {
        judgeIndex(index);
        data[index] = e;
    }

    // 判断数组中是否含有指定元素
    public boolean contains(E e) {
        for (int i = 0; i < size; i++) {
            if (data[i].equals(e))
                return true;
        }
        return false;
    }

    // 查找数组中元素e所在的索引，如果不存在元素e，则返回-1
    public int find(E e) {
        for (int i = 0; i < size; i++) {
            if (data[i].equals(e)) {
                return i;
            }
        }
        return -1;
    }

    // 从数组中删除index位置的元素, 返回删除的元素
    public E remove(int index) {
        judgeIndex(index);
        E ret = data[index];
        for (int i = index + 1; i < size; i++) {
            data[i - 1] = data[i];
        }
        size--;
        data[size] = null;
        if (size == data.length / 4 && data.length != 0) {
            reSize(data.length / 2);
        }
        return ret;
    }

    // 从数组中删除第一个元素, 返回删除的元素
    public E removeFirst() {
        return remove(0);
    }

    // 从数组中删除最后一个元素, 返回删除的元素
    public E removeLast() {
        return remove(size - 1);
    }

    // 从数组中删除元素e
    public void removeElement(E e) {
        int index = find(e);
        if (index != -1)
            remove(index);
    }

    public String toString() {
        StringBuilder res = new StringBuilder();
        res.append(String.format("Array:size=%d,capacity=%d\n", size, data.length));
        res.append("[");
        for (int i = 0; i < size; i++) {
            res.append(data[i]);
            if (i != size - 1)
                res.append(",");
        }
        res.append("]");
        return res.toString();
    }

    // 改变数组容量
    private void reSize(int newCapacity) {
        E[] newData = (E[]) new Object[newCapacity];
        for (int i = 0; i < size; i++)
            newData[i] = data[i];
        data = newData;
    }

    private void judgeIndex(int index) {
        if (index < 0 || index > size)
            throw new IllegalArgumentException(String.format("Index is illegal.Require index>=0 and index <=%d", size));
    }
}
