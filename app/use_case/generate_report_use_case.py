from app.repository.ship_repository import ShipRepository

class GenerateReportUseCase:
    
    def __init__(self, ship_repository: ShipRepository) -> None:
        self.ship_repository = ship_repository
        
    def execute(self, date: str):
        ships = self.ship_repository.get_by_date(date)
        total_price = sum(ship.price for ship in ships)
        
        return f"The date {date} was shipped {len(ships)} packages with a total price of {total_price}"