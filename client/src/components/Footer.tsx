"use client";
import React from "react";
import { cn } from  "@/lib/utils";
import { Tooltip } from "@/components/Tooltip";
import { motion } from "framer-motion";


function Footer({ className }: { className?: string }) {
  return (
    <footer className={cn(" text-neutral-500 py-6", className)}>
      <div className="max-w-6xl mx-auto px-4 ">
        <div className=" gap-8 flex justify-around ">
          <div className="space-y-4 w-[40%] grid-cols-1">
            <h4 className="text-lg font-semibold">About Us</h4>
            <p>
             treasure hunt is a game where players are given clues to find a hidden treasure or object. The game is usually played in teams and the first team to find the treasure wins. The game can be played indoors or outdoors and is a fun way to get people moving and working together.
            </p>
          </div>

        

          <div className="space-y-4">
            <h4 className="text-lg font-semibold">Contact Us</h4>
            <Tooltip></Tooltip>
            <p>
              <strong>Email:</strong> xyz@gmail.com
            </p>
            <p>
              <strong>Phone:</strong> 6969696969
            </p>
            <p>
              <strong>Address:</strong> Rizvi college
            </p>
          </div>
        </div>

      
      </div>


 

    </footer>
  );
}

export default Footer;
