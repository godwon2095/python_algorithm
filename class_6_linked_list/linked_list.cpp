#include "linked_list.hpp"
#include <iostream>

using namespace std;

BSTreeNode::BSTreeNode(const int &elem, BSTreeNode *leftPtr, BSTreeNode *rightPtr)
:element(elem),
left(leftPtr),
right(rightPtr)
{}


BSTree::BSTree()
{
    root = 0;
}


BSTree::~BSTree()
{
    DestroySub(root);
}

// 각 노드를 모두 돌면서 소멸
void BSTree::DestroySub(BSTreeNode *node)
{
    if (node)
    {
        DestroySub(node->left);
        DestroySub(node->right);
        delete node;
    }
}

// 삽임함수
void BSTree::insert(const int &newElement)
{
    insertSub(root, newElement);
}

// 부모 노드의 키값과 삽입될 키 값을 비교하여 부모 노드의 키 값보다 작으면 좌측에 삽입하고
// 그렇지 않으면 우측에 삽입한다.
void BSTree::insertSub(BSTreeNode *&p, const int &newElement)
{
    if (p == NULL)
    {
        p = new BSTreeNode(newElement, NULL, NULL);
        if (root == NULL)
        {
            root = p;
        }
    }
    else if (newElement < p->element)
        insertSub(p->left, newElement);
    else if (newElement > p->element)
    {
      insertSub(p->right, newElement);
    }
    else
        cout << "The element is already in the tree!" << endl;
}


// 검색함수
int BSTree::retrieve(int searchKey) const
{
    return retrieveSub(root, searchKey);
}


// 찾고있는 원소가 해당 노드의 원소와 같을 때 이를 출력한다.
int BSTree::retrieveSub(BSTreeNode *p, int searchKey) const
{
    if (p == NULL)
    {
        cout << "Not found!" << endl;
        return 0;
    }
    else if(searchKey < p->element)
        return retrieveSub(p->left, searchKey);
    else if (searchKey > p->element)
        return retrieveSub(p->right, searchKey);
    else
    {
        cout << "key : " << searchKey << " was found!" << endl;
        return 1;
    }
}


// 원소 삭제 함수
int BSTree::remove(int deleteKey)
{
    return removeSub(root, deleteKey);
}


// 1. 삭제할 노드의 오른쪽 자식이 없는 경우는 해당 노드의 부모의 해당 링크가 해당 노드의 왼쪽 링크와 같도록 한다.
// 2. 해당 노드의 오른쪽 자식은 있으나 왼쪽 자식이 없는 경우, 부모가 오른쪽 자식을 가리키도록 하고, 부모의 오른쪽의 왼쪽 링크가 부모의 왼쪽 링크를 가리키도록 하면 된다.
// 3. 위의 두 경우에 해당하지 않으면 오른쪽 부분나무에서 가장 작은 키를 찾아 해당 위치에 옮기고 가장 작은 키의 오른쪽 자식을 가장 작은 키의 부모의 왼쪽 자식으로 하게 한다.
int BSTree::removeSub(BSTreeNode *&p, int deleteKey)
{
    if (deleteKey < p->element)
        return removeSub(p->left, deleteKey);
    else if (deleteKey > p->element)
        return removeSub(p->right, deleteKey);
    else {
        cutRightmost(root, p);
        return 0;
    }
}


void BSTree::cutRightmost(BSTreeNode *&r, BSTreeNode *&delPtr)
{
    int item;

    BSTreeNode *itemPtr;

    itemPtr = delPtr;

    if (delPtr->left == NULL)
    {
        delPtr = delPtr->right;
        delete itemPtr;
    }
    else if (delPtr->right == NULL)
    {
        delPtr = delPtr->left;
        delete itemPtr;
    }
    else
    {
        GetProdecessor(delPtr->right, item);
        delPtr->element = item;
    }
}


void BSTree::GetProdecessor(BSTreeNode *p, int &deleteKey)
{
    while(p->left != NULL)
        p = p->left;
    int temp = p->right->element;
    removeSub(p->right, temp);
    deleteKey = p->element;
    p->element = temp;
}


void BSTree::showStructure() const
{
    if (root == NULL)
        cout << "Tree is empty" << endl;
    else
    {
        cout << endl;
        showSub(root, 1);
        cout << endl;
    }
}


void BSTree::showSub(BSTreeNode *p, int level) const
{
    int j;

    if (p != NULL)
    {
        showSub(p->right, level + 1);
        for (j = 0; j < level; j++)
            cout << "\t";
        cout << " " << p->element;
        if ((p->left != NULL) &&
            (p->right != NULL))
            cout << "<";
        else if (p->right != NULL)
            cout << "/";
        else if (p->left != NULL)
            cout << "\\";
        cout << endl;
        showSub(p->left, level + 1);
    }
}
