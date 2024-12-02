import uuid
from sqlmodel import Field, SQLModel
from typing import Optional, Any
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import Column

class CharacterTable(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    data: dict = Field(default_factory=dict, sa_column=Column(JSON))
    owner_id: Optional[uuid.UUID] = Field(default=None, foreign_key="usertable.id")  # Внешний ключ

class Attribute(SQLModel):
    value: int  # Значение атрибута
    modifier: int  # Модификатор атрибута

class Skill(SQLModel):
    proficient: bool  # Указывает, обладает ли персонаж навыком
    modifier: int  # Модификатор навыка

class Ability(SQLModel):
    name: str  # Название способности
    description: str  # Описание способности

class Spell(SQLModel):
    name: str  # Название заклинания
    level: int  # Уровень заклинания
    description: str  # Описание заклинания
    uses: int  # Количество использований заклинания

class Weapon(SQLModel):
    name: str  # Название оружия
    type: str  # Тип оружия
    damage: str  # Урон, наносимый оружием
    bonus: str  # Бонус к атаке или урону

class Armor(SQLModel):
    name: str  # Название брони
    armorClass: int  # Класс брони

class Item(SQLModel):
    name: str  # Название предмета
    description: str  # Описание предмета

class Health(SQLModel):
    maxHP: int  # Максимальные очки здоровья
    currentHP: int  # Текущие очки здоровья
    hitDice: str  # Кубик для определения очков здоровья

class Equipment(SQLModel):
    weapons: list[Weapon]  # Список оружия
    armor: Armor  # Броня
    items: list[Item]  # Список предметов

class Attributes(SQLModel):
    strength: Attribute
    dexterity: Attribute
    constitution: Attribute
    intelligence: Attribute
    wisdom: Attribute
    charisma: Attribute

class Skills(SQLModel):
    acrobatics: Skill
    intimidation: Skill
    stealth: Skill
    # Могут быть дополнительные поля для других навыков

class Character(SQLModel):
    name: str  # Имя персонажа
    player: str  # Имя игрока
    class_name: str  # Класс персонажа
    level: int = Field(..., ge=1)  # Уровень персонажа, должен быть больше или равен 1
    race: str  # Раса персонажа
    background: Optional[str] = Field(default=None, nullable=True)  # Предыстория персонажа
    alignment: Optional[str] = Field(default=None, nullable=True)  # Мировоззрение персонажа
    experience: Optional[int] = Field(default=None, ge=0, nullable=True)  # Опыт персонажа
    attributes: Optional[Attributes] = Field(default=None, nullable=True)  # Атрибуты персонажа
    skills: Optional[Skills] = Field(default=None, nullable=True)  # Навыки персонажа
    abilities: Optional[list[Ability]] = Field(default=None, nullable=True)  # Специальные способности
    spells: Optional[list[Spell]] = Field(default=None, nullable=True)  # Заклинания
    equipment: Optional[Equipment] = Field(default=None, nullable=True)  # Оборудование
    health: Optional[Health] = Field(default=None, nullable=True)  # Здоровье
    armorClass: Optional[int] = Field(default=None, ge=1, nullable=True)  # Класс брони
    initiative: Optional[int] = Field(default=None, nullable=True)  # Инициатива
    speed: Optional[int] = Field(default=None, ge=0, nullable=True)  # Скорость передвижения
    notes: Optional[str] = Field(default=None, nullable=True)  # Дополнительные заметки
