from abc import ABC, abstractmethod

# Product

class ProductButton(ABC):
    @abstractmethod
    def on_click(self):
        pass

class WinButton(ProductButton):
    def on_click(self):
        pass

class HTMLButton(ProductButton):
    def on_click(self):
        pass

# Creator

class CreatorDialog(ABC):
    @abstractmethod
    def create_button(self) -> ProductButton:
        pass

class CreatorWinDialog(CreatorDialog):
    def create_button(self) -> ProductButton:
        return WinButton()

class CreatorWebDialog(CreatorDialog):
    def create_button(self) -> ProductButton:
        return HTMLButton()


def client():
    button = CreatorWinDialog().create_button()
    button.on_click()

    button = CreatorWebDialog().create_button()
    button.on_click()