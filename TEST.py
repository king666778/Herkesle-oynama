"""Define a simple example game."""

# ba_meta require api 8

from __future__ import annotations

from typing import TYPE_CHECKING

import bascenev1 as bs
from bascenev1lib.game.deathmatch import DeathMatchGame

if TYPE_CHECKING:
    pass


# ba_meta export bascenev1.GameActivity
class MyGame(DeathMatchGame):
    """My first ballistica game!"""

    name = 'My Game!'

    def on_begin(self) -> None:
        super().on_begin()
        bs.screenmessage('KİNG666 HESABINIZ İYİ ÇALIYOR!!!!', color=(0, 1, 0))
        
