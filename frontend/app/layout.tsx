import "./globals.css"
export const metadata = { title: "Velix CRM", description: "Gestionale ISP Velix Srls" }
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return <html lang="it"><body className="bg-gray-50 text-gray-900">{children}</body></html>
}
