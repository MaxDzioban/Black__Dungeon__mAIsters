'''Module to work with Pylonomial through linked list'''

class Mono:
    '''Represents a single term in a polynomial'''
    def __init__(self, coefficient, degree) -> None:
        self.coefficient = coefficient
        self.degree = 0 if self.coefficient == 0 else degree
        self.next = None

    def __str__(self) -> str:
        res = 'Mono: '
        if self.coefficient == 0:
            return res + '0'
        if self.coefficient not in (-1, 1):
            res += str(self.coefficient)
        if self.coefficient == -1:
            res += '-'
        if self.coefficient in (1,-1) and self.degree == 0:
            res += '1'
        if self.degree != 0:
            res += 'x'
        if self.degree not in (0,1):
            res += '**' + str(self.degree)
        # print(res)
        return res

    def __repr__(self) -> str:
        return f'Mono(coeff={self.coefficient}, degree={self.degree})'

    def __eq__(self, value: 'Mono') -> bool:
        return isinstance(value, Mono) and \
(self.coefficient, self.degree) == (value.coefficient, value.degree)

class Polynomial:
    '''Represents a polynomial using a linked list of Mono objects'''
    def __init__(self, *args: list['Mono']) -> None:
        if isinstance(args[0], Polynomial):
            self.head = args[0].copy().head
            head = self.head
            args_h = args[0].copy().head.next
            while args_h:
                head.next = args_h
                head = head.next
                args_h = args_h.next
        else:
            self.head = Mono(args[0].coefficient, args[0].degree)
            head = self.head

        def get_rec_cof(next_: 'Mono'):
            nonlocal head
            if isinstance(next_, Mono):
                head.next = Mono(next_.coefficient, next_.degree)
                head = head.next
            else:
                while next_.head:
                    get_rec_cof(next_.head)
                    next_.head = next_.head.next

        for next_ in args[1:]:
            get_rec_cof(next_)

    def __str__(self) -> str:
        res = 'Polynomial: '
        head: 'Mono' = self.head
        while head:
            if head.coefficient not in (0,1,-1):
                res += str(head.coefficient)
            if len(res) == 12 and head.coefficient == 0 and head.next is None:
                res += '0'
            if head.coefficient == -1:
                res += '-'
            if head.coefficient in (1,-1) and head.degree == 0:
                res += '1'
            if head.degree != 0:
                res += 'x'
            if head.degree not in (0,1):
                res += '**'+str(head.degree)
            if head.next:
                res += '+' if head.next.coefficient > 0 and len(res) > 12 else ''

            head = head.next
        return res

    def __repr__(self) -> str:
        res = 'Polynomial('
        head: 'Mono' = self.head
        while head:
            # print('head: ', head, head.next)
            res += repr(head) + ' -> ' if head.next else repr(head)
            head = head.next
        # print(res)
        return res+')'

    @property
    def degree(self):
        '''Computes the degree of the polynomial'''
        max_ = None
        head: 'Mono' = self.head
        while head:
            if max_ is None:
                max_ = head.degree
            elif head.degree > max_:
                max_ = head.degree
            head = head.next
        return max_

    def copy(self):
        '''Creates a copy of the polynomial'''
        res = Polynomial(self.head)
        head_, head = res.head, self.head

        while head:
            head_.next = Mono(head.next.coefficient, head.next.degree) if head.next else None
            head_, head = head_.next, head.next

        return res

    def sort(self):
        '''Sorts the polynomial in descending order of degree'''
        # print()
        # print(f'FIRST_SORT: {repr(self)}')
        head = self.head
        end_ = 1
        while end_:
            counter = 1
            while head:
                if counter and head.next is not None and (head.next.degree > head.degree or \
(head.next.degree == head.degree == 0 and head.next.coefficient > head.coefficient)):

                    # print('if')
                    two = head.next
                    thr = head.next.next
                    head.next.next = head
                    head.next = thr
                    self.head = two

                    # print(repr(self))

                elif head.next is not None and head.next.next is not None and \
(head.next.next.degree > head.next.degree or (head.next.next.degree == head.next.degree == 0 \
and head.next.next.coefficient > head.next.coefficient)):
                    # print('elif')
                    fort = head.next.next.next
                    third = head.next.next
                    head.next.next.next = head.next
                    head.next.next = fort
                    head.next = third
                    # print(repr(self))

                # elif head.next is None:



                # print('sth_0')
                counter = 0
                head = head.next

                head_c = self.head
                end_ = 0
                while head_c:
                    if head_c.next is not None and (head_c.next.degree > head_c.degree or \
    (head_c.next.degree == head_c.degree == 0 and head_c.next.coefficient > head_c.coefficient)):
                        end_ = 1
                    head_c = head_c.next
                # print('sth_1')

                if not end_:
                    break
                # print('sth_2')
            head = self.head

    def simplify(self, wit_sort = 1):
        '''Simplifies the polynomial by combining like terms and removing terms with zero \
coefficients'''
        # print('\n\n\n')
        # print(f'OTHER: {repr(self)}')
        if wit_sort and self.head.coefficient and self.head.next:
            self.sort()

        # print(f'OTHER2: {repr(self)}')
        head = self.head
        while head:
            if head.next and head.degree == head.next.degree:
                head.coefficient += head.next.coefficient
                if head.coefficient == 0:
                    head.degree = 0
                head.next = head.next.next
                if head.next and head.degree == head.next.degree:
                    continue
            head = head.next

        head = self.head
        while head:
            if head.next and head.next.coefficient == 0:
                head.next = head.next.next
            head = head.next

        # print(repr(self))

        if wit_sort and self.head.coefficient and self.head.next:
            self.sort()

        # print('What I NEED', repr(self))

    def eval_at(self, val_x):
        '''Evaluates the polynomial at a given value of x'''
        res, head = 0, self.head
        while head:
            res += head.coefficient*(val_x**head.degree)
            head = head.next
        return res

    def __eq__(self, value: 'Polynomial') -> bool:
        # print()
        if not isinstance(value, Polynomial):
            return False

        self.simplify()
        value.simplify()

        head_1, head_2 = self.head, value.head
        while head_1 and head_2:
            if head_1 != head_2:
                # print(f'head_1: {head_1}, head_2: {head_2}')
                return False
            head_1, head_2 = head_1.next, head_2.next
        if head_1 != head_2:
            # print('f2')
            return False
        return True

    def __hash__(self) -> int:
        self.simplify()
        if self.head.coefficient and self.head.next:
            self.sort()

        res, head = '', self.head
        while head:
            res += str(head.coefficient+head.degree)
            head = head.next
        return int(res)

    @property
    def derivative(self):
        '''Computes the derivative of the polynomial'''
        # print()
        # print(repr(self))
        res = self.copy()
        # print(repr(res))
        head = res.head
        while head:
            head.coefficient *= head.degree
            if head.degree != 0:
                head.degree -= 1
            head = head.next

        # print(repr(res))

        res.simplify()

        # print(repr(self))
        # print(repr(res))
        return res

    def __add__(self, val: 'Polynomial'):
        # print()
        res = self.copy()
        head_1, head_2 = res.head, val.head
        while head_1.next:
            head_1 = head_1.next

        while head_2:
            # print(f'head_2: {head_2}')
            head_1.next = Mono(head_2.coefficient, head_2.degree) if head_2 else None
            head_1, head_2 = head_1.next, head_2.next

        # print(repr(res))

        res.simplify()

        # print(repr(res))

        return res

    def __sub__(self, val: 'Polynomial'):
        # print()
        res = self.copy()
        head_1, head_2 = res.head, val.head
        while head_1.next:
            head_1 = head_1.next

        while head_2:
            # print(f'head_2: {head_2}')
            head_1.next = Mono(-head_2.coefficient, head_2.degree) if head_2 else None
            head_1, head_2 = head_1.next, head_2.next

        # print(repr(res))

        res.simplify()

        # print(repr(res))

        return res

    def __mul__(self, val: 'Polynomial'):
        if isinstance(val, Polynomial):
            res = self.copy()
            copy_ = self.copy()
            head_2 = val.head
            head = Mono(0,0)
            res_ = head

            while head_2:
                head_1 = copy_.head
                while head_1:
                    head.next = Mono(head_1.coefficient*head_2.coefficient, \
head_1.degree+head_2.degree if head_1.coefficient*head_2.coefficient != 0 else 0)
                    head = head.next

                    head_1 = head_1.next

                head_2 = head_2.next

            cop = res_.next
            res.head = cop
            res_h = res.head
            while cop.next:
                res_h = cop.next
                res_h = res_h.next
                cop = cop.next

        if isinstance(val, int):
            res = self.copy()
            res_h = res.head
            while res_h:
                res_h.coefficient *= val
                if res_h.coefficient == 0:
                    res_h.degree = 0
                res_h = res_h.next

        res.simplify()

        return res

    def __rmul__(self, val: 'Polynomial'):
        if isinstance(val, Polynomial):
            res = self.copy()
            copy_ = self.copy()
            head_2 = val.head
            head = Mono(0,0)
            res_ = head

            while head_2:
                head_1 = copy_.head
                while head_1:
                    head.next = Mono(head_1.coefficient*head_2.coefficient, \
head_1.degree+head_2.degree if head_1.coefficient*head_2.coefficient != 0 else 0)
                    head = head.next

                    head_1 = head_1.next

                head_2 = head_2.next

            cop = res_.next
            res.head = cop
            res_h = res.head
            while cop.next:
                res_h = cop.next
                res_h = res_h.next
                cop = cop.next

        if isinstance(val, int):
            res = self.copy()
            res_h = res.head
            while res_h:
                res_h.coefficient *= val
                if res_h.coefficient == 0:
                    res_h.degree = 0
                res_h = res_h.next

        res.simplify()

        return res
