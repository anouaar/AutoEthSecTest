# AutoEthSecTest

Framework Python pour tester et sécuriser les communications diagnostiques automobiles (UDS/DoIP).

## Objectif
Automatiser les tests de conformité et de sécurité sur des ECU (simulés), en s'appuyant sur pytest.

## État actuel
- [x] Environnement pytest + CI-ready
- [x] Builder de requêtes UDS
- [ ] Parser de réponses UDS (positives/négatives)
- [ ] ECU simulé
- [ ] Fuzzing
- [ ] Dashboard
- [ ] Docker + CI

## Lancer les tests
    pip install -r requirements.txt
    pytest -v

## Stack
Python, pytest, UDS (ISO 14229), DoIP, CAN



