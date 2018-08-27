<?php

interface Human
{
    public function say();
}

class Man implements Human
{
    public function say()
    {
        echo '男人<br/>';
    }
}

class Woman implements Human
{
    public function say()
    {
        echo '女人<br/>';
    }
}

interface Factory
{
    public function createMan();
}

class ManFactory implements Factory
{
    public function createMan()
    {
        return new Man();
    }
}

class WomanFactory implements Factory
{
    public function createMan()
    {
        return new Woman();
    }
}

$man = new ManFactory();
$woman = new WomanFactory();
$manSay = $man->createMan();
$womanSay = $woman->createMan();
$manSay->say();
$womanSay->say();
