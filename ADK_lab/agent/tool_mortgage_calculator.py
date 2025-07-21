from ibm_watsonx_orchestrate.agent_builder.tools import *

@tool
def mortgage_calculator(loan_amount : float, annual_interest_rate : float, loan_term_years : int, down_payment: float) -> str:
    """
    Berekent de details van een hypotheeklening en retourneert het resultaat als een geformatteerde string. Alle invoer is vereist..

    :loan_amount (float): Totaal leenbedrag vóór aftrek van de aanbetaling.
    :annual_interest_rate (float): Jaarlijkse rente (in procent).
    :loan_term_years (int): Leningaflossingsperiode in jaren.
    :down_payment (float): Voorschot betaald.
    
    :returns: Geformatteerde hypotheeklening samenvatting.
    """
    # Převod vstupních hodnot
    principal = loan_amount - down_payment
    monthly_interest_rate = annual_interest_rate / 100 / 12
    number_of_payments = loan_term_years * 12

    # Případ nulové úrokové sazby
    if monthly_interest_rate == 0:
        monthly_payment = principal / number_of_payments
    else:
        monthly_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments) / \
                          ((1 + monthly_interest_rate) ** number_of_payments - 1)

    total_payment = monthly_payment * number_of_payments
    total_interest = total_payment - principal

    # Vytvoření formátovaného výsledného řetězce
    result = (
        f"--- Hypotheekoverzicht ---\n"
        f"Bedrag van de lening: {loan_amount:,.2f} Euro\n"
        f"Aanbetaling: {down_payment:,.2f} Euro\n"
        f"Leenbedrag na aanbetaling: {principal:,.2f} Euro\n"
        f"Rente: {annual_interest_rate:.2f} %\n"
        f"Terugbetalingsperiode: {loan_term_years} jaar\n\n"
        f"Maandelijkse termijn: {monthly_payment:,.2f} Euro\n"
        f"Totaal betaalde rente: {total_interest:,.2f} Euro\n"
        f"Totale kosten van de lening: {total_payment:,.2f} Euro\n"
    )

    return result
