import sys

# -----------------------------
# Node 클래스 (단순 연결 리스트용)
# -----------------------------
class Node:
    def __init__(self, elem, next=None):
        self.data = elem  # 데이터 필드 (Book 객체)
        self.link = next  # 링크 필드
    
    # 참고용: 현재 노드 다음에 새 노드 삽입
    def append(self, new):
        if new is not None:
            new.link = self.link
            self.link = new

    # 현재 노드의 다음 노드 삭제 후 반환
    def popNext(self):
        deleted_node = self.link
        if deleted_node is not None:
            self.link = deleted_node.link
        return deleted_node

# -----------------------------
# Book 클래스
# -----------------------------
class Book:
    """도서 객체의 정보를 저장"""
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"  - 번호: {self.book_id}, 제목: {self.title}, 저자: {self.author}, 출판연도: {self.year}"

# -----------------------------
# LinkedList 클래스
# -----------------------------
class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def clear(self):
        self.head = None

    def size(self):
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.link
        return count

    def getNode(self, pos):
        if pos < 0:
            return None
        node = self.head
        count = 0
        while count < pos and node is not None:
            node = node.link
            count += 1
        return node

    def insert(self, pos, elem):
        new_node = Node(elem)
        if pos == 0:
            new_node.link = self.head
            self.head = new_node
        else:
            prev = self.getNode(pos - 1)
            if prev is not None:
                new_node.link = prev.link
                prev.link = new_node

    def remove(self, pos):
        if pos < 0 or self.isEmpty():
            return None
        if pos == 0:
            deleted_node = self.head
            self.head = self.head.link
            return deleted_node
        else:
            prev = self.getNode(pos - 1)
            if prev is not None and prev.link is not None:
                deleted_node = prev.link
                prev.link = deleted_node.link
                return deleted_node
            else:
                return None

    def display(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.link

    def find_by_id(self, book_id):
        node = self.head
        while node is not None:
            if node.data.book_id == book_id:
                return node.data
            node = node.link
        return None

    def find_by_title(self, title):
        node = self.head
        while node is not None:
            if node.data.title == title:
                return node.data
            node = node.link
        return None

    def find_pos_by_title(self, title):
        node = self.head
        pos = 0
        while node is not None:
            if node.data.title == title:
                return pos
            node = node.link
            pos += 1
        return None

# -----------------------------
# BookManagement 클래스
# -----------------------------
class BookManagement:
    def __init__(self):
        self.books = LinkedList()

    def add_book(self):
        """새 도서 추가"""
        try:
            book_id = input("  > 책 번호: ")
            title = input("  > 책 제목: ")
            author = input("  > 저자: ")
            year = int(input("  > 출판 연도: "))
        except ValueError:
            print("\n[오류] 출판 연도는 숫자로 입력해야 합니다.")
            return

        if self.books.find_by_id(book_id) is not None:
            print(f"\n[오류] 이미 존재하는 책 번호({book_id})입니다.")
            return

        new_book = Book(book_id, title, author, year)
        self.books.insert(self.books.size(), new_book)
        print(f"\n[성공] '{title}' 도서가 추가되었습니다.")

    def remove_book(self):
        """책 제목으로 도서 삭제"""
        title = input("  > 삭제할 책 제목: ")
        pos = self.books.find_pos_by_title(title)
        if pos is not None:
            self.books.remove(pos)
            print(f"\n[성공] '{title}' 도서가 삭제되었습니다.")
        else:
            print(f"\n[오류] '{title}' 도서를 찾을 수 없습니다.")

    def search_book(self):
        """책 제목으로 도서 조회"""
        title = input("  > 조회할 책 제목: ")
        book = self.books.find_by_title(title)
        if book is not None:
            print("\n[조회 결과]")
            print(book)
        else:
            print(f"\n[오류] '{title}' 도서를 찾을 수 없습니다.")

    def display_books(self):
        """전체 도서 목록 출력"""
        print("\n--- [ 전체 도서 목록 ] ---")
        if self.books.isEmpty():
            print("현재 등록된 도서가 없습니다.")
        else:
            self.books.display()
        print("--------------------------")

    def run(self):
        """메뉴 실행"""
        while True:
            print("\n===== 도서 관리 프로그램 =====")
            print("  1. 도서 추가")
            print("  2. 도서 삭제 (책 제목으로 삭제)")
            print("  3. 도서 조회 (책 제목으로 조회)")
            print("  4. 전체 도서 목록 출력")
            print("  5. 프로그램 종료")
            print("============================")
            
            choice = input("  > 메뉴 선택 (1-5): ")

            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.remove_book()
            elif choice == '3':
                self.search_book()
            elif choice == '4':
                self.display_books()
            elif choice == '5':
                print("\n프로그램을 종료합니다.")
                sys.exit()
            else:
                print("\n[오류] 잘못된 입력입니다. 1에서 5 사이의 숫자를 입력하세요.")

# -----------------------------
# 프로그램 실행
# -----------------------------
if __name__ == "__main__":
    app = BookManagement()
    app.run()