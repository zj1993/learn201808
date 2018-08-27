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

class SimpleFactory
{
    public static function Man()
    {
        return new Man();
    }

    public static function Woman()
    {
        return new Woman();
    }
}


$man = SimpleFactory::Man();
$woman = SimpleFactory::Woman();
$man->say();
$woman->say();