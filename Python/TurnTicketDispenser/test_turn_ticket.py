import unittest

from turn_ticket import TicketDispenser, TurnTicket, TurnNumberSequence

class TicketDispenserTest(unittest.TestCase):

    def setUp(self):
        TurnNumberSequence._turnNumber = -1

    def test_do_something(self):
        dispenser = TicketDispenser()
        ticket = dispenser.getTurnTicket()
    
    def test_TurnTicket_turnnumber_property_validation(self):
        turn_ticket = TurnTicket(20)

        assert turn_ticket.turnNumber == 20
    
    def test_turn_number_sequence_is_incremental(self):

        assert TurnNumberSequence.next_turn_number() == 0
        assert TurnNumberSequence.next_turn_number() == 1

    def test_single_dispenser_creates_different_sequential_tickets(self):

        dispenser = TicketDispenser()
        ticket = dispenser.getTurnTicket()
        ticket2 = dispenser.getTurnTicket()
        assert ticket.turnNumber == 0
        assert ticket2.turnNumber == 1

    def test_multiple_dispensers_create_different_sequential_tickets(self):
         dispenser1 = TicketDispenser()
         dispenser2 = TicketDispenser()
         ticket1 = dispenser1.getTurnTicket()
         ticket2 = dispenser2.getTurnTicket()
         ticket3 = dispenser1.getTurnTicket()

         assert ticket1.turnNumber == 0
         assert ticket2.turnNumber == 1
         assert ticket3.turnNumber == 2

         


if __name__ == "__main__":
	unittest.main()
     
# Test cases
# validate turnticket property, turnnumber
# test increase in turn number sequence
# Test single dispenser creates different tickets sequentially
# test multiple dispensers create different sequential tickets