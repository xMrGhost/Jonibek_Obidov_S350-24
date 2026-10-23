def funk_S350_24_JOU(massiv):
    """15-raqam: Berilgan massivdagi eng katta elementni topish"""
    if not massiv:
        return None
    eng_katta = massiv[0]
    for son in massiv:
        if son > eng_katta:
            eng_katta = son
    return eng_katta

# Test
print(funk_S350_24_JOU([4, 67, 34, 98]))
print("Branch JOU dan qo'shilgan o'zgarish")