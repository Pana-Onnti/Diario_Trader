from sqlalchemy.orm import Session
from db.models.models import Trade
from db.schemas.schema_trade import TradeOut  ,TradeDict
from crud import *
class TradeController:
    def __init__(self, db: Session):
        self.db = db
    
    async def create_trade(self, email: str, trade: TradeDict):
        try:
            validar_usuario_cuenta(self.db, email)
        except:
            pass
        db_trade = trade_nuevo(self.db, trade, email)
        return db_trade
    
    async def get_trades_by_email(self, email: str):
        usuario = obtener_usuario_por_email_db(self.db, email)
        if usuario is None:
            raise UsuarioNoExisteException()
        trades = [] 
        for cuenta in usuario.cuentas:
            trades_cuenta = [TradeDict.from_orm(trade) for trade in cuenta.trades]
            trades.append(trades_cuenta)
        return trades
    
    async def get_all_trades(self):
        trades = self.db.query(Trade).all()
        return [TradeOut(**trade.__dict__).dict() for trade in trades]
    
    async def delete_trade_by_id(self, trade_id: int):
        trade = self.db.query(Trade).filter(Trade.Id == trade_id).first()
        if trade is None:
            raise HTTPException(status_code=404, detail="Trade not found")
        self.db.delete(trade)
        self.db.commit()
        return {"message": "Trade deleted"}
