import click
from clients.services import ClientsServices
from clients.models import Client

@click.group()
def client():
    """Manages the client life cicle"""
    pass


@client.command()
@click.option('-n', '--name', type = str, prompt = True, help = 'The client name')
@click.option('-c', '--company', type = str, prompt = True, help = 'The client company')
@click.option('-e', '--email', type = str, prompt = True, help = 'The client email')
@click.option('-p', '--position', type = str, prompt = True, help = 'The client position')
@click.pass_context
def create(ctx, name, company, email, position):
    """Create a new client"""
    client = Client(name, company, email, position)
    client_service = ClientsServices(ctx.obj['clients_table'])

    client_service.create_client(client)

    


@client.command()
@click.pass_context
def lists (ctx):
    """List all Clients"""
    client_service = ClientsServices(ctx.obj['clients_table'])

    clients_list = client_service.list_clients()

    click.echo('|  ID  |  NAME  |  COMPANY  |  EMAIL  |  POSITION  |')
    click.echo('')
    click.echo('='*75)
    for client in clients_list:
        click.echo('|  {uid}  |  {name}  |  {company}  |  {email}  |  {position}  |'.format(uid = client['uid'], name = client['name'],
                                                                                        company = client['company'], email = client['email'],
                                                                                        position = client['position'], ))


    


@client.command()
@click.option('-id', '--client_uid', type = str, prompt = True, help = 'The id of the client to update')
@click.pass_context
def update(ctx, client_uid):
    "Update client information"
    client_service = ClientsServices(ctx.obj['clients_table'])
    client_list = client_service.list_clients()

    client = [client for client in client_list if client['uid'] == client_uid]

    if client:
        client = _updated_client_flow(Client(**client[0]))
        client_service.update_client(client)

        click.echo('Client updated')
    else:
        click.echo( 'Client not found')


def _updated_client_flow(client):
    click.echo('Leave empty if you dont want to modify the client')
    
    client.name = click.prompt('New name', type = str, default = client.name)
    client.company = click.prompt('New company', type = str, default = client.company)
    client.email = click.prompt('New email', type = str, default = client.email)
    client.position = click.prompt('New name', type = str, default = client.position)

    return client


@client.command()
@click.option('-id', '--client_uid', type = str, prompt = True, help = 'The id of the client to update')
@click.pass_context
def delete(ctx, client_uid):
    """Delete the information of a client"""
    client_service = ClientsServices(ctx.obj['clients_table'])
    client_list = client_service.list_clients()

    client = [client for client in client_list if client['uid'] == client_uid]

    if client:
        client_service.delete_client(Client(**client[0]))
        click.echo( 'The client was deleted')


    


all = client