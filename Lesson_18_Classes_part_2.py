from hero import *


myhero = Hero("Drujok", 4, "Pets")
mysuperhero = SuperHero("Andres", 10, "Apostoles", 5, 50)
mysuperhero1 = SuperHero("Kisa", 7, "Humans", 4, 35)

myhero.show_hero()
mysuperhero.show_hero()

myhero.show_hero()
mysuperhero1.show_hero()

mysuperhero1.makemagic()
mysuperhero1.show_hero()

mysuperhero.makemagic()
mysuperhero.makemagic()
mysuperhero.show_hero()


mysuperhero.magic = 10 + mysuperhero.magiclevel
mysuperhero.show_hero()
