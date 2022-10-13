import Omega
import pytest


class TestOmega:
    def teste_basemontador_1(self):
        string = "asdf"
        o = Omega.Omega(string, 0)
        assert o.base_montador(len(string)) == ([12,4,1])
    def teste_basemontador_2(self):
        string = "matheus"
        o = Omega.Omega(string, 0)
        assert o.base_montador(len(string)) == ([2520, 840, 210, 42, 7, 1])
    def teste_basemontador_um(self):
        string = "a"
        o = Omega.Omega(string,0)
        assert o.base_montador(len(string)) == ([])
    def teste_gera_montador_1(self):
        string = "asdf"
        o = Omega.Omega(string, 0)
        assert o.gera_montador(4,o.base_montador(len(string))) == ([0,1,0])
    def teste_gera_montador_2(self):
        string = "matheus"
        o = Omega.Omega(string, 0)
        assert o.gera_montador(600,o.base_montador(len(string))) == ([0, 0, 2, 4, 1, 5])
    def teste_permuta(self):
        string = "matheus"
        o = Omega.Omega(string, 0)
        assert o.permuta(o.gera_montador(600,o.base_montador(len(string))),list(string)) == (["u","h","t","s","m","e","a"])
    def teste_permuta_2(self):
        string = "matheus"
        o = Omega.Omega(string, 0)
        assert o.permuta(o.gera_montador(5039,o.base_montador(len(string))),list(string)) == (["a","t","h","e","u","s","m"])