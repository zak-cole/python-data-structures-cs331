class ConstrainedList(list):
    """Constrains the list class so it offers only the following primitive array API:

        - `lst[i]` for getting and setting a value at an *existing, positive* index `i`
        - `len(lst)` to obtain the number of slots
        - `lst.append(None)` to grow the list by *one slot at a time*
        - `del lst[len(lst)-1]` to delete the last slot in a list

       All other operations will result in an exception being raised.
    """

    # NOT MINE
    # credit to prof. Matthew Bauer

    def __init__(self, *args):
        super().__init__(*args)

    def append(self, value):
        if value is not None:
            raise ValueError('Can only append None to constrained list!')
        super().append(value)

    def __getitem__(self, idx):
        if idx < 0 or idx >= len(self):
            raise ValueError('Can only use positive, valid indexes on constrained lists!')
        return super().__getitem__(idx)

    def __setitem__(self, idx, value):
        if idx < 0 or idx >= len(self):
            raise ValueError('Can only use positive, valid indexes on constrained lists!')
        super().__setitem__(idx, value)

    def __delitem__(self, idx):
        if idx != len(self) - 1:
            raise ValueError('Can only delete last item in constrained list!')
        super().__delitem__(idx)

    def __getattribute__(self, name):
        if name in ('insert', 'pop', 'remove', 'min', 'max',
                    'index', 'count', 'clear', 'copy', 'extend'):
            raise AttributeError('Method "' + name + '" not supported on constrained list!')
        else:
            return super().__getattribute__(name)

    # __getattribute__ isn't called for special methods, so the following are needed

    def __add__(self, value):
        raise AttributeError('Constrained lists do not support `+`!')

    def __contains__(self, value):
        raise AttributeError('Constrained lists do not support `in`!')

    def __eq__(self, value):
        raise AttributeError('Constrained lists do not support `==`!')

    def __iter__(self):
        raise AttributeError('Constrained lists do not support iteration!')

    def __str__(self):
        raise AttributeError('Constrained lists do not support stringification!')

    def __repr__(self):
        raise AttributeError('Constrained lists do not support stringification!')

    # for testing only! (don't use this in your ArrayList implementation)

    def _as_list(self):
        return list(super().__iter__())
