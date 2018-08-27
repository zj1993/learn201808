<?php

interface Target
{
    public function ps2();
    public function usb();
}

class ps2
{
    public function ps2Interface()
    {
        return 'ps2接口<br/>';
    }
}

class usb implements Target
{
    private $ps2;

    function __construct(ps2 $ps2)
    {
        $this->ps2 = $ps2;
    }

    public function ps2()
    {
        echo $this->ps2->ps2Interface();
    }

    public function usb()
    {
        echo 'usb接口<br/>';
    }
}

class Client
{
    public static function main()
    {
        $ps2 = new ps2();
        $usb = new usb($ps2);
        $usb->ps2();
        $usb->usb();
    }
}

Client::main();
