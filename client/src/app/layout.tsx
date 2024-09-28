
import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import Navbar from "@/components/Navbar";
const inter = Inter({ subsets: ["latin"] });
export const metadata: Metadata = {
  title: "Treasure Hunt",
  description: "Find the treasure and win exciting prizes",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  
  return (
    <html lang="en">
      <body className={inter.className}>
      <Navbar className="top-9"/>
      {children}
    </body>
  </html>
  );
}
