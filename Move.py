class Move:

    def __init__(self, piece, new_position, piece_to_capture=None):
        self.notation = None
        self.check = False
        self.checkmate = False
        self.kingSideCastle = False
        self.queenSideCastle = False

        self.piece = piece
        self.oldPos = piece.position
        self.newPos = new_position
        self.pieceToCapture = piece_to_capture
        self.specialMove = None
        self.rookMove = None

    def __eq__(self, other):
        if self.oldPos == other.oldPos and \
                self.newPos == other.newPos and \
                self.specialMove == other.specialMovePiece:
            if not self.specialMove:
                return True
            if self.specialMove and \
               self.specialMove == other.specialMovePiece:
                return True
            else:
                return False
        else:
            return False
