"use client";
import React, { useState } from "react";
import { HoveredLink, Menu, MenuItem, ProductItem } from "./ui/navbar-menu";
import { cn } from "@/lib/utils";
import Link from "next/link";

function Navbar({ className }: { className?: string }) {
  const [active, setActive] = useState<string | null>(null);
  
  
  return (
    <div className={cn("fixed top-10 inset-x-0 max-w-2xl mx-auto z-50", className)}>
  <Menu setActive={setActive}>
    <Link href="/">
      <MenuItem setActive={setActive} active={active} item="Home" />
    </Link>
    <Link href="/Digital-Quiz">
    <MenuItem setActive={setActive} active={active} item="Digital-Quiz">
     
    </MenuItem>
    </Link>
    <MenuItem setActive={setActive} active={active} item="Live-Stats">
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 p-4 text-sm sm:text-base">
        <ProductItem
          title="Current Teams"
          href="/teams"
          src="https://images.pexels.com/photos/163064/play-stone-network-networked-interactive-163064.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
          description="Curent teams playing in the treasure hunt."
        />
        <ProductItem
          title="Live Leaderboard"
          href="/leaderboard"
          src="https://plus.unsplash.com/premium_photo-1676673189412-56a98d221c11?q=80&w=2500&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
          description="position of the teams in the leaderboard."
        />
        <ProductItem
          title="CC-assist"
          href="/CC-assist"
          src="https://plus.unsplash.com/premium_photo-1661302846246-e8faef18255d?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
          description="Admin page to manage the treasure hunt."
        />
        
      </div>
    </MenuItem>

    {/* Commented out section for future use */}
    {/* <MenuItem setActive={setActive} active={active} item="Plans">
      <div className="flex flex-col space-y-4 text-sm sm:text-base">
        <HoveredLink href="/free-plan">Free Plan</HoveredLink>
        <HoveredLink href="/premium-plan">Premium Plan</HoveredLink>
      </div>
    </MenuItem> */}
    
     <MenuItem setActive={setActive} active={active} item="Authenticate">
      <div className="flex flex-col space-y-4 text-sm sm:text-base">
        <HoveredLink href="/Signup">Register</HoveredLink>
        <HoveredLink href="/Login">Login-In</HoveredLink>
      </div>
    </MenuItem>
   
    
  </Menu>
</div>

  );
}

export default Navbar;
