class Move:

    def __init__(self, piece, new_position, piece_to_capture=None):
        self.notation = None
        self.check = False
        self.checkmate = False
        self.special_move = None
        self.king_side_castle = False
        self.queen_side_castle = False
        self.rook_move = None

        self.piece = piece
        self.old_pos = piece.position
        self.new_pos = new_position
        self.piece_to_capture = piece_to_capture

    def __eq__(self, other):
        if self.old_pos == other.old_pos and \
                self.new_pos == other.new_pos and \
                self.special_move == other.specialMove:
            if not self.special_move:
                return True
            if self.special_move and \
               self.special_move == other.specialMove:
                return True
            else:
                return False
        else:
            return False
