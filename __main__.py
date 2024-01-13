from app.use_case.create_client_use_case import CreateClientUseCase
from app.use_case.create_ship_use_case import CreateShipUseCase
from app.use_case.generate_report_use_case import GenerateReportUseCase
from app.domain.city import City
from app.repository.client_repository import ClientRepository
from app.repository.ship_repository import ShipRepository

if __name__ == "__main__":
    client_repository = ClientRepository()
    ship_repository = ShipRepository()
    
    create_client_use_case = CreateClientUseCase(client_repository)
    
    client = create_client_use_case.execute('1', 'andres')
    
    create_ship_use_case = CreateShipUseCase(ship_repository)
    
    ship = create_ship_use_case.execute(City.MEDELLIN, City.CALI, client.id)
    
    generate_report_use_case = GenerateReportUseCase(ship_repository)
    
    report = generate_report_use_case.execute('2024-01-12')

    print(report)