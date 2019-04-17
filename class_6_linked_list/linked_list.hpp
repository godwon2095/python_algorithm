// 수학과 2015110417 장성원
#ifndef linked_list_hpp
#define linked_list_hpp

// linked_list 형태
class BSTreeNode
{
private:
    BSTreeNode(const int &elem, BSTreeNode *leftPtr, BSTreeNode *rightPtr);

    int element;
    BSTreeNode *left,
    *right;

    friend class BSTree;
};


class BSTree
{
public:
    BSTree(); // 생성자
    ~BSTree(); // 소멸자
    void DestroySub(BSTreeNode *node); // 소멸자 보조 함수

    void insert(const int &newElement); // 원소 삽입 함수
    int retrieve(int searchKey) const; // 원소 검색 함수
    int remove(int deleteKey); // 원소 삭제 함수

    void showStructure() const; // 현재 이진트리의 구조 보여주는 함수

private:
    void insertSub(BSTreeNode *&p, const int &newElement); // 원소 삽입 보조함수
    int retrieveSub(BSTreeNode *p, int searchKey) const; // 원소 검색 보조함수
    int removeSub(BSTreeNode *&p, int deleteKey); // 원소 삭제 보조함수
    void GetProdecessor(BSTreeNode *p, int &deleteKey); // 삭제를 위한 그 전 원소 찾는 함수
    void cutRightmost(BSTreeNode *&r, BSTreeNode *&delPtr); // 오른 쪽 날려버리는 함수
    void showSub(BSTreeNode *p, int level) const; // 이진트리 구조 보여즈는 보조함수

    BSTreeNode *root;
};

#endif
