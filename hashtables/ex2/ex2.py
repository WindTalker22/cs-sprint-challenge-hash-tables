#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = [None] * length  # Create big enough list
    flights = {}

    for ticket in tickets:
        if ticket.source == 'NONE':
            first_flight = ticket

        flights[ticket.source] = ticket.destination

    route[0] = first_flight.destination

    for i in range(1, length):
        source = route[i - 1]

        route[i] = flights[source]

    return route
