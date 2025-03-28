package main

type MyStack struct {
	q1 []int
}

func Constructor() MyStack {
	return MyStack{}
}

func (this *MyStack) Push(x int) {
	this.q1 = append(this.q1, x)
	for i := 0; i < len(this.q1); i++ {
		this.q1 = append(this.q1, this.q1[0])
		this.q1 = this.q1[1:]
	}
}

func (this *MyStack) Pop() int {
	item := this.q1[0]
	this.q1 = this.q1[1:]
	return item
}

func (this *MyStack) Top() int {
	if this.Empty() {
		return -1
	}
	return this.q1[0]
}

func (this *MyStack) Empty() bool {
	return len(this.q1) == 0
}
