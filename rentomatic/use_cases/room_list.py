from rentomatic.repository.interface import IRepository


def room_list_use_case(repo: IRepository):
    return repo.list()
